document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll('.posts .post .body').forEach((element) => {
        let text = element.innerHTML;
        let words = text.split(/[\s,]+/);
        let maxWords = 20;

        if (words.length > maxWords) {
            let truncatedText = words.slice(0, maxWords).join(' ') + `...<a href="${element.previousElementSibling.innerHTML}">Смотреть пост</a>`;
            element.innerHTML = truncatedText;
        } else {
            let truncatedText = words.slice(0, maxWords).join(' ') + `...<a href="${element.previousElementSibling.innerHTML}">Смотреть пост</a>`;
            element.innerHTML = truncatedText;
        }
    })

    setTimeout(() => {
        phone1()
    }, 10000)

    document.querySelector('.phone').onmouseover = () => {
        document.querySelector('.phone').style.background = '#FF1F00';
        document.querySelector('.phone').style.color = '#fff';
    }
    document.querySelector('.phone').onmouseout = () => {
        document.querySelector('.phone').style.background = '#fff';
        document.querySelector('.phone').style.color = '#000000';
    }
    
    document.querySelectorAll('.call').forEach((element) => {
        element.addEventListener("click", (event) => {
            document.querySelector('.phone-call').style.display = 'grid';
        })
    })

    document.querySelector('.phone-call').addEventListener("click", (event) => {
        if (event.srcElement.className === "phone-call") {
            document.querySelector('.phone-call').style.display = 'none';
        }
    })    

    function phone1() {
        document.querySelector('.phone').style.background = '#FF1F00';
        document.querySelector('.phone').style.color = '#fff';
        setTimeout(() => {
            document.querySelector('.phone').style.background = '#fff';
            document.querySelector('.phone').style.color = '#000000';
        }, 300)
        setTimeout(() => {
            phone2()
        }, 25000)
    }
    function phone2() {
        document.querySelector('.phone').style.background = '#FF1F00';
        document.querySelector('.phone').style.color = '#fff';
        setTimeout(() => {
            document.querySelector('.phone').style.background = '#fff';
            document.querySelector('.phone').style.color = '#000000';
        }, 300)
        setTimeout(() => {
            phone1()
        }, 25000)
    }


    document.addEventListener("scroll", (event) => {
        if (window.scrollY + window.innerHeight >= document.body.scrollHeight) {
            document.querySelector('.phone').style.background = '#FF1F00';
            document.querySelector('.phone').style.color = '#fff';
            setTimeout(() => {
                document.querySelector('.phone').style.background = '#fff';
                document.querySelector('.phone').style.color = '#000000';
            }, 300)
        }

        if (window.scrollY <= document.querySelector('#navbar').offsetHeight) {
            document.querySelector('#navbar').style.boxShadow = 'none';
        } else {
            document.querySelector('#navbar').style.boxShadow = '0 2px 6px rgba(0, 0, 0, 0.10)'
        }
    })

    document.querySelector('.up').addEventListener("click", (event) => {
        document.documentElement.scrollTo({
            top: 0,
            behavior: "smooth"
        });
    })


});
