$('.navToggle').on('click', function (e) {
  e.preventDefault();
  $('body').toggleClass('navToggleActive');
});


$(window).scroll(function () {
  if ($(this).scrollTop() > 10) {
    $('body').addClass('fixedHeader');
  } else {
    $('body').removeClass('fixedHeader');
  }
});


var swiper = new Swiper(".testimonialSwiper", {
  navigation: {
    nextEl: ".test-swiper-button-next",
    prevEl: ".test-swiper-button-prev",
  },
});


var swiper = new Swiper(".certificatesSlider", {
  slidesPerView: 1,
  spaceBetween: 16,
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
  navigation: {
    nextEl: ".cert-swiper-button-next",
    prevEl: ".cert-swiper-button-prev",
  },
  breakpoints: {
    640: {
      slidesPerView: 2,
      spaceBetween: 16,
    },
    768: {
      slidesPerView: 2,
      spaceBetween: 16,
    },
    1024: {
      slidesPerView: 2,
      spaceBetween: 16,
    },
  },
});



var icon = document.getElementById('icon');
if (icon) {
  icon.addEventListener('click', function () {
    let mode = this.dataset.mode
    setTheme(mode)
  });
}

let theme = localStorage.getItem('theme')

if (theme == null) {
  setTheme("dark")
}
else {
  setTheme(theme)
}



function setTheme(mode) {
  console.log(mode)
  if (icon) {
    if (mode == "dark") {
      icon.src = "static/images/sun.png"
      icon.dataset.mode = "light"
      document.getElementById('theme-style').href = 'static/css/darkTheme.css'
    }
    else {
      icon.src = "static/images/moon.png"
      icon.dataset.mode = "dark"
      document.getElementById('theme-style').href = 'static/css/style.css'
    }
    localStorage.setItem('theme', mode)
  }
  else {
    if (mode == "dark") {
      document.getElementById('theme-style').href = '/static/css/darkTheme.css'
    }
    else {
      document.getElementById('theme-style').href = '/static/css/style.css'
    }
    localStorage.setItem('theme', mode)
  }
}



