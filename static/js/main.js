const charBox = document.getElementById('char-box')
const loadBtn = document.getElementById('load-btn')
let visible = 10


const handleGetData = () => {
    $.ajax({
        type: 'GET',
        url: `${page}/json-details/${visible}`,
        success: function (response) {
            max_size = response.max
            const data = response.data
            data.map(character => {
                charBox.innerHTML += `            
            <tr>
            <td>${ character.name }</td>
            <td>${ character.height }</td>
            <td>${ character.mass }</td>
            <td>${ character.hair_color }</td>
            <td>${ character.skin_color }</td>
            <td>${ character.eye_color }</td>
            <td>${ character.birth_year }</td>
            <td>${ character.gender }</td>
            <td>${ character.homeworld }</td>
            <td>${ character.date }</td>
            </tr>`
            })
            if (max_size) {
                loadBox.innerHTML = "<h4>No more characters to load</h4>"
            }
        },
        error: function (error) {
            console.log(error)
        }
    })

}

    handleGetData()
loadBtn.addEventListener('click', () => {
    visible += 10
    handleGetData()
})