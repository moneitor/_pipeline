//////////////////////////////////////////////////////////////////////////////////
// Creates a covariance matrix using the position of the points and its difference
// with the centroid of all the points together.
//////////////////////////////////////////////////////////////////////////////////


vector arrayPos[];
vector pos;
vector currPt;
vector center = set(0,0,0);

for (int i = 0 ; i< @numpt ; i++) {
    pos = point( 0 , "P" , i);
    append(arrayPos , pos);
    center += pos;
}

center /= @numpt;

float v11 = 0 , v12 = 0 , v13 = 0,
      v21 = 0 , v22 = 0 , v23 = 0,
      v31 = 0 , v32 = 0 , v33 = 0;

foreach (currPt ; arrayPos){
    v11 += (currPt.x - center.x) * (currPt.x - center.x);
    v12 += (currPt.x - center.x) * (currPt.y - center.y);
    v13 += (currPt.x - center.x) * (currPt.z - center.z);
    v21 += (currPt.x - center.x) * (currPt.y - center.y);
    v22 += (currPt.y - center.y) * (currPt.y - center.y);
    v23 += (currPt.y - center.y) * (currPt.z - center.z);
    v31 += (currPt.x - center.x) * (currPt.z - center.z);
    v32 += (currPt.y - center.y) * (currPt.z - center.z);
    v33 += (currPt.z - center.z) * (currPt.z - center.z);
}


3@mat = set(v11 , v12 , v13,
            v21 , v22 , v23,
            v31 , v32 , v33);
            
matrix3 identDiv = ident() * (1/3.0);
matrix3 newMat = transpose(3@mat) * (3@mat);  

3@mat = newMat * identDiv;
            
            


//////////////////////////////////////////////////////////////////////////////////
// Creates a orthogonal matrix using the covariance matrix created by the previous function.
//////////////////////////////////////////////////////////////////////////////////

matrix3 myTM = 3@mat;

matrix3 invMyTM = invert(myTM);                   
                   
vector eiInit = set(1,1,1);

function vector eigenVector(vector eigenVal ; matrix3 myMatrix ; float errorMax){

    float errorEstimate = 100;
    float oldEigen = 0;
    
    while(errorEstimate  > errorMax) {

        eigenVal = eigenVal * myMatrix;
    
        float maxC = max(eigenVal);
        
        errorEstimate = ((maxC - oldEigen)/ maxC) * 100;
    
        vector newEigen = set(eigenVal.x / maxC , eigenVal.y / maxC , eigenVal.z / maxC);
    
        eigenVal = newEigen;
    
        oldEigen = maxC;
    
        }
        
        eigenVal = normalize(eigenVal);
        return eigenVal;
        
}

float allow_error = chf("max_error_allowed");

vector eigenA = eigenVector(eiInit , myTM , allow_error);
vector eigenB = eigenVector(eiInit , invMyTM , allow_error);


setpointattrib(0 , "eigenA" , @ptnum , eigenA );

setpointattrib(0 , "eigenB" , @ptnum , eigenB );

            
       


//////////////////////////////////////////////////////////////////////////////////////////
// Creates an array containing all the half edges and an integer with the amount of them//
//////////////////////////////////////////////////////////////////////////////////////////  
            
            
            
int count = 0;

int hedge = pointhedge(0, @ptnum);
int hedges[];

while(hedge != -1) {
    append(hedges, hedge);
    int nextHedge = pointhedgenext(0, hedge);
    count++;
    
    hedge = nextHedge;
}

i[]@hedges = hedges;
i@count = count;
            


//////////////////////////////////////////////////////////////////////////////////////////
// Return a lot of useful information from the half edges connected to the current point//
//////////////////////////////////////////////////////////////////////////////////////////  

int count = 0;

int hedge = pointhedge(0, @ptnum);
int hedges[];
int connectedPoints[]; 
float distances[];
float avgDistance;
float maxDistance;
float minDistance;


while(hedge != -1) {
    append(hedges, hedge);
    int connectedPoint = hedge_dstpoint(0, hedge);       
    append(connectedPoints, connectedPoint);
    
        
    float dist = length(v@P - point(0, "P", connectedPoint));
    append(distances, dist);    
   
    
    int nextHedge = pointhedgenext(0, hedge);
    
    
    hedge = nextHedge;
}

i[]@hedges = hedges;
i[]@connectedPoints = connectedPoints;
f[]@distances = distances;


f@avgDistance = avg(distances);
f@maxDistance = max(distances);
f@minDistance = min(distances);




//////////////////////////////////////////////////////////////////////////////////////////
// Forces a vector MyVector to be orthogonal to vector Norm//
//////////////////////////////////////////////////////////////////////////////////////////  

vector G = v@v;
vector N = v@N;

vector ForceTangent(vector Norm; vector MyVector){
/*This function takes vector MyVector and forces it to be orthogonal to the vector 
Norm, so it is tangent to the surface from which Norm is created, Norm should be the Normal 
of the surface*/
    vector Perpendicular = (dot(MyVector , Norm) / dot(Norm, Norm)) * Norm ;
    Perpendicular = MyVector - Perpendicular;
    float mag = length(MyVector);
    Perpendicular = normalize(Perpendicular);
    
    return Perpendicular * mag;
    
}

//New gradient vector tangent to the surface
v@v = ForceTangent(N , G);
          




//////////////////////////////////////////////////////////////////////////////////////////
// Creates an FK dependency between the points, where each points inherit the TM of its
// Previous point//
////////////////////////////////////////////////////////////////////////////////////////// 



matrix oldMat = ident();
float totalPoints = float(@numpt);



for(int point = 0 ; point < @numpt ; point++) {
    vector pos0 = point(0 , "P" , 0);
    float noiseFreq = chf("noise_Freq") * 0.1;
    float noiseSpeed = chf("Noise_speed");
    float noiseAmp = chf("noise_Amp") * 0.1;
    float noiseM = snoise(point* (noiseFreq) + @Time* noiseSpeed + (pos0 * 100)) * noiseAmp;
    
    
    matrix myMat = ident();
    //get the normalized value along the entire curve
    float bias = float(point)/totalPoints;
    //calculate one vector that points tangent to the line
    vector tangent = (point(0,"P", point) - point(0,"P" , point -1));
    
    //if the point is not zero, then the matrix is gonna be translated
    //in the direction of the tangent by the magnitud of the same vector
    if(point!=0){
        translate(myMat , (normalize(tangent) * length(tangent)));  
    }
    //this curve modifies the bias of the angle along the curve
    float curl = chramp("bias" , bias);
    
    matrix3 rotAlong= maketransform( set(0,0,1) , set(0,1,0) );
    float sineAlong = sin(bias);
    
    //in here we rotate the current matrix  
    //rotate(myMat , radians(chf("angle") * curl) , set(1,0,0));
    rotate(myMat , noiseM * curl , set(1,0,0));
    rotate(rotAlong , radians(chf("rotate_along_axis") * sineAlong)  , normalize(tangent));
    
    //in here we multiply the current matrix times the previous matrix, since in
    //point 0 the matrix was the identity, point 0 is gonna still the same
    myMat*= rotAlong;
    myMat *= oldMat;
    
    //we store the position in this variable, multipling an empty vector * my mat
    vector newPos = pos0 * myMat;
    
    //we set old mat to be the current matrix, so in the next iteration we have access
    //to the previous matrix
    oldMat = myMat;
    
    addattrib(0 , "point" , "myMat" , myMat);
    addattrib(0 , "point" , "tangent" , tangent);
        
    setpointattrib(0 , "tangent" , point , tangent , "set");
    setpointattrib(0, "P" , point , newPos , "set");
    setpointattrib(0, "noise" , point , noiseM , "set");
    
    
    
    
}

