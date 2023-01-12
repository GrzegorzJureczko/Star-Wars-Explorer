const nameBtn = document.getElementById('name-btn')
const heightBtn = document.getElementById('height-btn')
const massBtn = document.getElementById('mass-btn')
const hairColorBtn = document.getElementById('hair_color-btn')
const skinColorBtn = document.getElementById('skin_color-btn')
const eyeColorBtn = document.getElementById('eye_color-btn')
const birthYearBtn = document.getElementById('birth_year-btn')
const genderBtn = document.getElementById('gender-btn')
const homewroldBtn = document.getElementById('homeworld-btn')
const dateBtn = document.getElementById('date-btn')

const nameColData = document.querySelectorAll('tr')
const heightColData = document.querySelectorAll('tr')
const massColData = document.querySelectorAll('tr')
const hairColorColData = document.querySelectorAll('tr')
const skinColorColData = document.querySelectorAll('tr')
const eyeColorColData = document.querySelectorAll('tr')
const birthYearColData = document.querySelectorAll('tr')
const genderColData = document.querySelectorAll('tr')
const homewroldColData = document.querySelectorAll('tr')
const dateColData = document.querySelectorAll('tr')


nameBtn.addEventListener('click', () => {
    nameColData.forEach((item) => {
        if (item.children[0].classList.contains('d-none')) {
            nameBtn.classList.remove('btn-secondary')
            nameBtn.classList.add('btn-primary')
            item.children[0].classList.remove('d-none')
        } else {
            nameBtn.classList.remove('btn-primary')
            nameBtn.classList.add('btn-secondary')
            item.children[0].classList.add('d-none')
        }
    })
})

heightBtn.addEventListener('click', () => {
    heightColData.forEach((item) => {
        if (item.children[1].classList.contains('d-none')) {
            heightBtn.classList.remove('btn-secondary')
            heightBtn.classList.add('btn-primary')
            item.children[1].classList.remove('d-none')
        } else {
            heightBtn.classList.remove('btn-primary')
            heightBtn.classList.add('btn-secondary')
            item.children[1].classList.add('d-none')
        }
    })
})

massBtn.addEventListener('click', () => {
    massColData.forEach((item) => {
        if (item.children[2].classList.contains('d-none')) {
            massBtn.classList.remove('btn-secondary')
            massBtn.classList.add('btn-primary')
            item.children[2].classList.remove('d-none')
        } else {
            massBtn.classList.remove('btn-primary')
            massBtn.classList.add('btn-secondary')
            item.children[2].classList.add('d-none')
        }
    })
})

hairColorBtn.addEventListener('click', () => {
    hairColorColData.forEach((item) => {
        if (item.children[3].classList.contains('d-none')) {
            hairColorBtn.classList.remove('btn-secondary')
            hairColorBtn.classList.add('btn-primary')
            item.children[3].classList.remove('d-none')
        } else {
            hairColorBtn.classList.remove('btn-primary')
            hairColorBtn.classList.add('btn-secondary')
            item.children[3].classList.add('d-none')
        }
    })
})

skinColorBtn.addEventListener('click', () => {
    skinColorColData.forEach((item) => {
        if (item.children[4].classList.contains('d-none')) {
            skinColorBtn.classList.remove('btn-secondary')
            skinColorBtn.classList.add('btn-primary')
            item.children[4].classList.remove('d-none')
        } else {
            skinColorBtn.classList.remove('btn-primary')
            skinColorBtn.classList.add('btn-secondary')
            item.children[4].classList.add('d-none')
        }
    })
})

eyeColorBtn.addEventListener('click', () => {
    eyeColorColData.forEach((item) => {
        if (item.children[5].classList.contains('d-none')) {
            eyeColorBtn.classList.remove('btn-secondary')
            eyeColorBtn.classList.add('btn-primary')
            item.children[5].classList.remove('d-none')
        } else {
            eyeColorBtn.classList.remove('btn-primary')
            eyeColorBtn.classList.add('btn-secondary')
            item.children[5].classList.add('d-none')
        }
    })
})

birthYearBtn.addEventListener('click', () => {
    birthYearColData.forEach((item) => {
        if (item.children[6].classList.contains('d-none')) {
            birthYearBtn.classList.remove('btn-secondary')
            birthYearBtn.classList.add('btn-primary')
            item.children[6].classList.remove('d-none')
        } else {
            birthYearBtn.classList.remove('btn-primary')
            birthYearBtn.classList.add('btn-secondary')
            item.children[6].classList.add('d-none')
        }
    })
})



genderBtn.addEventListener('click', () => {
    genderColData.forEach((item) => {
        if (item.children[7].classList.contains('d-none')) {
            genderBtn.classList.remove('btn-secondary')
            genderBtn.classList.add('btn-primary')
            item.children[7].classList.remove('d-none')
        } else {
            genderBtn.classList.remove('btn-primary')
            genderBtn.classList.add('btn-secondary')
            item.children[7].classList.add('d-none')
        }
    })
})

homewroldBtn.addEventListener('click', () => {
    homewroldColData.forEach((item) => {
        if (item.children[8].classList.contains('d-none')) {
            homewroldBtn.classList.remove('btn-secondary')
            homewroldBtn.classList.add('btn-primary')
            item.children[8].classList.remove('d-none')
        } else {
            homewroldBtn.classList.remove('btn-primary')
            homewroldBtn.classList.add('btn-secondary')
            item.children[8].classList.add('d-none')
        }
    })
})

dateBtn.addEventListener('click', () => {
    dateColData.forEach((item) => {
        if (item.children[9].classList.contains('d-none')) {
            dateBtn.classList.remove('btn-secondary')
            dateBtn.classList.add('btn-primary')
            item.children[9].classList.remove('d-none')
        } else {
            dateBtn.classList.remove('btn-primary')
            dateBtn.classList.add('btn-secondary')
            item.children[9].classList.add('d-none')
        }
    })
})