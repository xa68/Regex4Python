const coll = document.getElementsByClassName("collapsible");

Array.prototype.forEach.call(coll, element => {
  element.addEventListener("click", () => {
    element.classList.toggle("active");
    const content = element.nextElementSibling;
    content.style.maxHeight = content.style.maxHeight ? null : content.scrollHeight + "px";
  });
});
