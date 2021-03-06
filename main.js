// Modules to control application life and create native browser window
const {app, BrowserWindow, ipcMain} = require('electron')
const path = require('path')
const { exec } = require('child_process');
const axios = require('axios').default;

const createWindow = () => {
    // Create the browser window.
    const mainWindow = new BrowserWindow({
        width: 1400,
        height: 900,
        webPreferences: {
            nodeIntegration: true,
            preload: path.join(__dirname, 'preload.js')
        }
    })

    let python = require('child_process').spawn('python', ['./backend/app.py']);
    python.stdout.on('data', function (data) {
        console.log("data: ", data.toString());
    });
    python.stderr.on('data', (data) => {
        console.log(`stderr: ${data}`); // when error
    });

    // and load the index.html of the app.
    mainWindow.loadFile('web/index.html')

    // Open the DevTools.
    mainWindow.webContents.openDevTools()
}

function uploadFiles(event, filePaths){
    axios.put('http://127.0.0.1:5000/data', filePaths)
        .then(function (response) {
            console.log("It says: ", response.data);
        })
        .catch(function (error) {
            console.log("There was an error: ", error);
        });

}


// This method will be called when Electron has finished
// initialization and is ready to create browser windows.
// Some APIs can only be used after this event occurs.
app.whenReady().then(() => {
    ipcMain.on("upload-files", uploadFiles)
    createWindow()

    app.on('activate', () => {
        // On macOS it's common to re-create a window in the app when the
        // dock icon is clicked and there are no other windows open.
        if (BrowserWindow.getAllWindows().length === 0) createWindow()
    })
})

// Quit when all windows are closed, except on macOS. There, it's common
// for applications and their menu bar to stay active until the user quits
// explicitly with Cmd + Q.
app.on('window-all-closed', () => {
    exec('taskkill /f /t /im app.exe', (err, stdout, stderr) => {
        if (err) {
            console.log(err)
            return;
        }
        console.log(`stdout: ${stdout}`);
        console.log(`stderr: ${stderr}`);
    });
    if (process.platform !== 'darwin') app.quit()
})

// In this file you can include the rest of your app's specific main process
// code. You can also put them in separate files and require them here.