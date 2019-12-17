let html = "";
const get_result = "{{o}}";
const leng = "{{leng}}";
var i;

for (i = 0; i < leng; i++) {
  result = get_result[i];

  html += '<div class="container" id="result">';
  html += '<div class="container" id="result">';
  html += '<div class="row">';
  html += '<div class="col-12 col-md-12">';
  html +=
    '<div class="single-special text-center wow fadeInUp" data-wow-delay="0.2s">';
  html += '<h4 style="text-align: left;">';
  html += result["title"];
  html += "</h4>";
  html += '<p style="text-align: left; color: blue;"> ';
  html += result["url"];
  html += "</p>";
  html += ' <p style="text-align: left;"> ';
  html += result["description"];
  html += "</p>";
  html += "</div>";
  html += "</div>";
  html += "</div>";
  html += "</div>";
}
