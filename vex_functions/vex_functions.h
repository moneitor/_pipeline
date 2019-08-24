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

            
            
            
            
            
            
            
          