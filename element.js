class Canvas extends HTMLElement{
  construction(){
    // super();

    this.onclick = function(){
      console.log("okey");
    }

  }

}
window.customElements.define('e-canva', Canvas);
