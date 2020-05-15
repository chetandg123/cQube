import base64


class Data():
    #path should be chrome.exe file location
    Path =executable_path="/home/chetan/PycharmProjects/cQube/Driverfile/chromedriver"


    URL = base64.b64decode("aHR0cHM6Ly9jcXViZS50aWJpbHByb2plY3RzLmNvbQ==").decode("utf-8")
    username = base64.b64decode("dGliaWxzb2x1dGlvbnNAY3F1YmUuY29t").decode("utf-8")
    password= base64.b64decode("dGliaWwxMjM=").decode("utf-8")

    email = "//input[@id='exampleInputEmail']"
    pwd = "//input[@id='exampleInputPassword']"
    loginbtn = "//button[@type='submit']"



    zoom_in = "//a[@title='Zoom in']"
    zoom_out = "//a[@title='Zoom out']"

    Blocks ="//button[@class='btn btn-secondary']/b[contains(text(),'Blocks')]"
    Clusters ="//button[@class='btn btn-secondary']/b[contains(text(),'Clusters')]"
    Schools  ="//button[@class='btn btn-secondary']/b[contains(text(),'Schools')]"

    District ="//select[@name='myDistrict']"

    Distoptions = "//select[@name='myDistrict']/option"
    year = "//select[@id='year']/option[1]"
    monthnames = "//select[@id='month']/option"
    august = "//select[@id='month']/option[contains(text(),'August')]"
    Sept = "//select[@id='month']/option[contains(text(),' September')]"
    Oct = "//select[@id='month']/option[contains(text(),' October ')]"

    dots = "leaflet-interactive"
    blockslist = "//select[@name='myBlock']/option"
    clusterlist ="//select[@name='myCluster']/option"
    reg_user = "//a"
    back = "//a"


    details="//div[@class='col-sm-4']/span"
    dist1 = "//select[@name='myDistrict']/option[1]"
    blk1 = "//select[@name='myBlock']/option[1]"
    clu1 = "//select[@name='myCluster']/option[1]"

    dist2 ="//select[@name='myDistrict']/option[2]"
    blk2 ="//select[@name='myBlock']/option[2]"
    clu2 = "//select[@name='myCluster']/option[2]"

    dist3="//select[@name='myDistrict']/option[2]"
    blk3 ="//select[@name='myBlock']/option[2]"
    clu3="//select[@name='myCluster']/option[2]"

    dist4 = "//select[@name='myDistrict']/option[4]"
    blk4 = "//select[@name='myBlock']/option[4]"
    clu4 = "//select[@name='myCluster']/option[4]"

    dist5 = "//select[@name='myDistrict']/option[5]"
    blk5 = "//select[@name='myBlock']/option[5]"
    clu5 = "//select[@name='myCluster']/option[5]"

    dist6 = "//select[@name='myDistrict']/option[6]"
    blk6 = "//select[@name='myBlock']/option[6]"
    clu6 = "//select[@name='myCluster']/option[6]"

    dist7 = "//select[@name='myDistrict']/option[7]"
    blk7 = "//select[@name='myBlock']/option[7]"
    clu7 = "//select[@name='myCluster']/option[7]"

    dist8 = "//select[@name='myDistrict']/option[8]"
    dist9 = "//select[@name='myDistrict']/option[9]"
    dist10 = "//select[@name='myDistrict']/option[10]"
    dist11 = "//select[@name='myDistrict']/option[11]"
    dist12= "//select[@name='myDistrict']/option[12]"
    dist13 = "//select[@name='myDistrict']/option[13]"
    dist14 = "//select[@name='myDistrict']/option[14]"
    dist15 = "//select[@name='myDistrict']/option[15]"
    dist16 = "//select[@name='myDistrict']/option[16]"
    dist17 = "//select[@name='myDistrict']/option[17]"
    dist18 = "//select[@name='myDistrict']/option[18]"
    dist19 = "//select[@name='myDistrict']/option[19]"
    dist20 = "//select[@name='myDistrict']/option[20]"

    hyper_link = "//p/span"
    directory ="//p[contains(text(),' Semester report for:')]/span"
    Download ="//img[@title='Download Report']"
# Dash board
    Dashboard ="//span[@class='" \
               "mat-button-wrapper']/mat-icon"
    login_in = "//span[@class='span']"
    SAR = "//div[@class='mat-list-item-content']/td[contains(text(),'Student')]"
    TAR ="//div[@class='mat-list-item-content']/td[contains(text(),'Teacher')]"
    SR  = "//div[@class='mat-list-item-content']/td[contains(text(),'Semester')]"
    crc ="//div[@class='mat-list-item-content']/td[contains(text(),'CRC Reports')]"
    Log_out ="//button/span[contains(text(),'Log Out')]"
    Home_icon ="//img[@id='home']"

    students = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-map-view/div/div[4]/div[1]/span"
    schoolcount = " /html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-map-view/div/div[4]/div[2]/span"
    DateRange =  "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-map-view/div/div[4]/div[3]/span"

    # xpath of Dashboard

    crcvisits = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-bar-chart/div/div[5]/div[1]/span"
    totalschools= "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-bar-chart/div/div[5]/div[2]/span"

    visited = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-bar-chart/div/div[5]/div[3]/span"
    notvisited = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-bar-chart/div/div[5]/div[4]/span"

    range = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-bar-chart/div/div[5]/div[5]/span"

    # Table in CRC

    # rowby data
    distrows = "//tr[@class='odd']/td"
    headers = "//th"

    # X axis and Y axis

    xaxis = "//select[@name='xAxis']/option"
    yaxis = "//select[@name='yAxis']/option"

    crcdistrict = "//select[@name='myDistrict']/option"
    selecttype ="//*[@id='select']/select/option"

    dload = "//img[@alt='Download Report']"
    Notemsg = "//div[@class='col-sm-12']/p/b"








