const apiKEY = "af82e65c2bba944f34ed74d01c8cd560";
const apiURL = "https://api.openweathermap.org/data/2.5/weather?units=metric";
const searchbox = document.querySelector('.city-input');
const searchBtn = document.querySelector('.search-button');


async function checkweather(city) {
    const response = await fetch(`${apiURL}&q=${city}&appid=${apiKEY}`);
    var data = await response.json();

    console.log(data);

    document.querySelector(".place").innerHTML = data.name;
    document.querySelector(".temp").innerHTML = Math.round(data.main.temp) + '°C';
    document.querySelector(".humid").innerHTML = data.main.humidity + '%';
    document.querySelector(".Wind").innerHTML = data.wind.speed + " km/hr";
}

searchBtn.addEventListener("click", () => {
    const city = searchbox.value;
    if (city) {
        checkweather(city);
    } else {
        alert("Please enter a city name.");
    }
});