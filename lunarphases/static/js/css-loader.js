window.css_files.forEach(css_file => {
  var linkElement = document.createElement("link");
  linkElement.rel = "stylesheet";
  linkElement.href = css_file;
  document.head.appendChild(linkElement);
});