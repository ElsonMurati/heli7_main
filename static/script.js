var slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
  showSlides(slideIndex += n);
}

function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}
    if (n < 1) {slideIndex = slides.length}
    for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
    }
    for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
    }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
}

<script>
    $(document).ready(function () {
        $('form').on('submit', function (e) {
            e.preventDefault();
            
            var query = $('input[name="query"]').val();
            
            $.ajax({
                url: '/search',
                type: 'GET',
                data: { query: query },
                success: function (data) {
                    // Update the search results section with the data received
                    $('#search-results').html(data);
                }
            });
        });
    });
</script>