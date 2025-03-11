import requests
import os
import json
import permavar as pv
import subprocess
import sys
import time


def makeDirectory(directoryName):
    if not os.path.exists(directoryName):
        os.makedirs(directoryName)
        return f"Directory '{directoryName}' created successfully."
    else:
        return f"Directory '{directoryName}' already exists."

def deleteFile(filePath):
    try:
        if os.path.exists(filePath):
            os.remove(filePath)
            return f"File '{filePath}' deleted successfully."
        else:
            return f"File '{filePath}' does not exist."
    except Exception as e:
        return f"An error occurred: {e}"

def runEXE(filePath):
    try:
        result = subprocess.run(filePath, check=True, shell=True)
        return f"Execution completed with return code: {result.returncode}"
    except subprocess.CalledProcessError as e:
        return f"An error occurred while running the .exe: {e}"

def extractDomain(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return data.get("domain", "Domain not found")
    except Exception as e:
        return f"An error occurred: {e}"
    
def extractURL(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return data.get("exe", "EXE not found")
    except Exception as e:
        return f"An error occurred: {e}"

directory = "temp/"

def convertToRawUrl(githubUrl):
    if "github.com" not in githubUrl or "/blob/" not in githubUrl:
        return "Invalid GitHub URL"
    
    rawUrl = githubUrl.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/")
    return rawUrl


def download(url, filename):
    fileloc = directory + filename

    r = requests.get(convertToRawUrl(url))

    f = open(fileloc,'w')
    f.write(r.content.decode())

def downloadBinary(url, filename):
    fileloc = directory + filename
    r = requests.get(convertToRawUrl(url))

    f = open(fileloc,'wb')
    f.write(r.content)

def pvUpdate(permavar:pv.PermaVar, var, content):

    data: dict = permavar.get(var)
    data.update(content)

    permavar.set(var, data)

def runAOTL(filename):

    exeURL = extractURL(filename)
    domain = extractDomain(filename)

    downloadBinary(exeURL, "current.exe")
    pvUpdate(data, "domains", {domain: exeURL})
    runEXE("temp\\current.exe")

def runURL(url):

    download(url, "install.aotl")
    runAOTL("temp\\install.aotl")

# Startup

makeDirectory("data")
makeDirectory("temp")
data = pv.PermaVar("", "data")
data.set("version", 0.1)
data.set("domains", {})
deleteFile("temp/current.exe")
deleteFile("temp/install.aotl")
domains = data.get("domains")

if len(sys.argv) > 1:
    url = sys.argv[1]

else:
    print("NO URL PROVIDED")
    time.sleep(3)
    sys.exit(1)


if url in domains:
    url = domains[url]


runURL(url)


