document.addEventListener("DOMContentLoaded", function () {
    const scrollLeftButton = document.querySelector(".scroll-left");
    const scrollRightButton = document.querySelector(".scroll-right");
    const bookShelf = document.querySelector(".book-shelf");
  
    scrollLeftButton.addEventListener("click", function () {
        bookShelf.scrollBy({
            left: -200,
            behavior: "smooth"
        });
    });
  
    scrollRightButton.addEventListener("click", function () {
        bookShelf.scrollBy({
            left: 200,
            behavior: "smooth"
        });
    });
  });
  
  
  
  
  function searchBooks() {
    var searchInput = document.getElementById("searchInput").value.toLowerCase();
    var books = document.querySelectorAll(".book img");
  
    books.forEach(function(book) {
        var altText = book.alt.toLowerCase();
        if (altText.includes(searchInput)) {
            book.closest('.book').style.display = "inline-block";
        } else {
            book.closest('.book').style.display = "none";
        }
    });
  }
  
  
 /* function scrollToBottom() {
    window.scrollTo({
        top: document.body.scrollHeight,
        behavior: 'smooth'
    });
  }
  
  window.addEventListener('scroll', function() {
    if (window.scrollY > 500) {
        document.querySelector('.scroll-down-button').style.display = 'block';
    } else {
        document.querySelector('.scroll-down-button').style.display = 'none';
    }
  });*/
