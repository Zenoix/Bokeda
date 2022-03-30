let dropZone = document.getElementById("file_upload");

function dropHandler(ev) {
  dragOverEndHandler()
}

function dragOverHandler(ev) {
  dropZone.setAttribute("filehover", "1");
}

function dragOverEndHandler() {
  dropZone.removeAttribute("filehover");
}

function uploadFiles() {
  let files = dropZone.files;
  let prompt;
  if (files.length === 0) {
    alert("No files uploaded. Please select or drop in your csv files.");
    return;
  }
  let fileNames="";
  for(let i = 0; i < files.length; i++){
    let fileName = files[i].name
    if (!/^[a-z0-9_.@()-]+\.csv$/i.test(fileName)){
      alert("Non-csv file uploaded. Bokeda only accepts csv files.")
      cancelFiles(false);
      return;
    }
    fileNames += fileName + "\n";
    console.log(files[i].path)
  }
  prompt = "Uploaded file(s):\n---------------------\n" + fileNames + "\nDo you wish to continue?";
  let result = electronAPI.confirmFileUpload()
  // if (confirm(prompt)){
  //   // TODO handle file upload to backend
  //   return;
  // }
}

function cancelFiles(cancelConfirm = true) {
  if (dropZone.files.length === 0) {
    alert("No files uploaded. Please select or drop in your csv files.");
    return;
  }
  if (cancelConfirm){
    if (!confirm("Are you sure you want to reset the files uploaded?")) {
      return;
    }
  }
  dropZone.value = '';

  if(!/safari/i.test(navigator.userAgent)){
    dropZone.type = '';
    dropZone.type = 'file';
  }
}
