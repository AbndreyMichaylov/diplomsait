let resultText = document.getElementsByClassName('result')[0];
let fileSelector = document.getElementsByClassName('file_selector')[0];
let loadImage = document.getElementsByClassName('load_image')[0];
let sendButton = document.getElementsByClassName('send_button')[0];
let langSelector = document.getElementsByClassName('language_selector')[0];
let downloadedImage = document.getElementsByClassName('downloaded_img')[0];
let copyToClipboardBtn = document.getElementsByClassName('copy_to_clipboard')[0];
let loadImageSrc = 'static/images/load2.gif';


sendButton.addEventListener('click', translate, false);
console.log(copyToClipboardBtn);
copyToClipboardBtn.addEventListener('click', async function(){
    var resText = await resultText.select();
    document.execCommand("copy");
}, false);


async function translate(){
    resultText.hidden = true;
    let selectedFile = fileSelector.files[0];
    let selectedLang = langSelector.value;
    let fileName = uuidv4() + '.png';
    if(selectedFile === undefined){
        alert('Файл не выбран');
        return;
    }
    let formData = new FormData();
    formData.append("photo", selectedFile);
    formData.append("lang", selectedLang);
    formData.append("photo_name", fileName);
    //console.log(formData["lang"]);

    const headers = new Headers({
        'Accept': 'application/json',
        "X-CSRFToken": document.getElementsByName('csrfmiddlewaretoken')[0].value
    });

    loadImage.src = loadImageSrc;

    let saveImageResponse = await fetch('upload/', {method: "POST", headers , body: formData})
    .then((response) => {
        return response.json();
    }).then((data) => {
        return data;
    });
    
    downloadedImage.src = saveImageResponse['image_root'];

    let translateImageResponse = await fetch('translate/', {method: "POST", headers , body: formData})
    .then((response) => {
        return response.json();
    }).then((data) => {
        return data;
    });

    loadImage.src = '';
    resultText.hidden = false;
    let translatedText = translateImageResponse['result'];
    resultText.innerHTML = translatedText;
}

function uuidv4() {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
      var r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
      return v.toString(16);
    });
  }