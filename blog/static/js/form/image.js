document.addEventListener("DOMContentLoaded", function() {
    // Get the file upload field element
    const fileInput = document.querySelector('.custom-image-upload-class');

    // If the element doesn't exist, terminate the script
    if (!fileInput) return;

    // Hide the element
    fileInput.style.display = 'none';

    // Create a button for file upload
    const uploadButton = document.createElement('button');
    uploadButton.innerText = 'Upload';
    uploadButton.type = 'button';
    uploadButton.className = 'btn-primary small w-button';  // Added class

    // Create an element to display the file name
    const fileNameDisplay = document.createElement('p');
    fileNameDisplay.className = 'filenamedisplayclass';  // Added class

    // Create a div element for wrapping and add a class
    const wrapperDiv = document.createElement('div');
    wrapperDiv.className = 'customuploadbutton';

    // Place the button and file name display element inside the wrapper
    wrapperDiv.appendChild(uploadButton);
    wrapperDiv.appendChild(fileNameDisplay);

    // Insert the wrapper after the hidden file upload field
    fileInput.parentNode.insertBefore(wrapperDiv, fileInput.nextSibling);

    // When clicking the button, trigger a "click" on the hidden file upload field
    uploadButton.addEventListener('click', function() {
        fileInput.click();
    });

    // When a file is selected, display its name
    fileInput.addEventListener('change', function() {
        if (fileInput.files.length) {
            fileNameDisplay.innerText = fileInput.files[0].name;
        } else {
            fileNameDisplay.innerText = '';
        }
    });

    // If a file was previously uploaded and is in cache
    const cachedFileName = fileInput.getAttribute('data-cached-filename');
    if (cachedFileName) {
        fileNameDisplay.innerText = cachedFileName;
    }
});
