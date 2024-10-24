const siteUrl = '//127.0.0.1:8000/';
const styleUrl = siteUrl + 'static/css/recipebookmarklet.css';
const minWidth = 250;
const minHeight = 250;

// load CSS
var head = document.getElementsByTagName('head')[0];
var link = document.createElement('link');
link.rel = 'stylesheet';
link.type = 'text/css';
link.href = styleUrl + '?r=' + Math.floor(Math.random() * 9999999999999999);
head.appendChild(link);

// load HTML
var body = document.getElementsByTagName('body')[0];
boxHtml = `
  <div id="recipebookmarklet">
    <a href="#" id="close">&times;</a>
    <h1>Select an image to bookmark:</h1>
    <div class="recipeimages"></div>
   </div>`;
body.innerHTML += boxHtml;

function recipebookmarkletLaunch() {
    recipebookmarklet = document.getElementById('recipebookmarklet');
    var recipeimagesFound = recipebookmarklet.querySelector('.recipeimages');
    // clear images found
    recipeimagesFound.innerHTML = '';
    // display bookmarklet
    recipebookmarklet.style.display = 'block';
    // close event
    recipebookmarklet.querySelector('#close')
        .addEventListener('click', function () {
            recipebookmarklet.style.display = 'none'
        });
    // find images in the DOM with the minimum dimensions
    recipeimages = document.querySelectorAll('img[src$=".jpg"], img[src$=".jpeg"], img[src$=".png"]');
    recipeimages.forEach(recipeimage => {
        if (recipeimage.naturalWidth >= minWidth
            && recipeimage.naturalHeight >= minHeight) {
            var recipeimageFound = document.createElement('img');
            recipeimageFound.src = recipeimage.src;
            recipeimagesFound.append(recipeimageFound);
        }
    })
    // select image event
    recipeimagesFound.querySelectorAll('img').forEach(recipeimage => {
        recipeimage.addEventListener('click', function (event) {
            recipeimageSelected = event.target;
            recipebookmarklet.style.display = 'none';
            window.open(siteUrl + 'recipeimages/create/?url='
                + encodeURIComponent(recipeimageSelected.src)
                + '&title='
                + encodeURIComponent(document.title),
                '_blank');
        })
    })
}
// launch the bookmkarklet
recipebookmarkletLaunch();