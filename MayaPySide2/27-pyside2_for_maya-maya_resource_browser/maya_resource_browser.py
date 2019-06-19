import maya.app.general.resourceBrowser as resourceBrowser


def get_resource_path():
    resource_browser = resourceBrowser.resourceBrowser()
    resource_path = resource_browser.run()

    return resource_path


if __name__ == "__main__":
    resource_path = get_resource_path()
    if resource_path:
        print(resource_path)
