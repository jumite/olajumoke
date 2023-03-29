const loader = document.querySelector('.loader_cont')

window.addEventListener('load', function(){
    this.setTimeout(myload, 2000)
})
function myload (){
    loader.style.display = 'none';
    document.body.style.overflow = 'auto';
}