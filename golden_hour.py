# Golden Hour App V1

# Description:
# ...
#    ...
#       ...


# API DATA NEEDED
# Pull data from a weather api
# pull data from a sun position api
# pull data from a time api
# pull data from a location api


# FEATURES

#  ...
# First step: figure out how to physically determine when golden hour is based on your location.
#
#
#
#
#

# Pseudocode

# SUN
# show map, get current location, or pick location...
# use geolocation to get sun angle
#
# AM
# Code after pm in reverse

# PM
# If sun degree too high ==> its before golden hour
# elif correct degree top >= current sun degree >= correct degree bottom  , ==> its during golden hour
#
#
#
#


# WEATHER
# Get weather data for location
# is the weather going to be good at the times?
# tell user, warn user, show user...
#   use simple html emojis???
#   click to open google weather

# TASKS
# -route to home page, and any other pages
# -gui in web (html flask templates with css?)
#       +background color/style
#       +images/assets from procreate
#       +text
#       +buttons (do we need JS here?)
#       +date/time/location/coordinates input field
#       +output text
#
# -eventually host, maybe on github
# -import any python packages needed
# -logic behind input forms, buttons, etc
# -logic behind pulling the
# -
# -
# -
# -
# -
# -
# -
# -
#
#
#

#
# ERRORS/BUGS
#       git@github.com: Permission denied (publickey).
#       Git fatal: could not read from remote repository


const
navSlide = () = > {
    const
burger = document.querySelector('.burger');
const
nav = document.querySelector('.navbar-nav');
const
navLinks = document.querySelectorAll('.navbar-nav li');

burger.addEventListener('click', () = > {
                                        // Toggle
Nav
nav.classList.toggle('navbar-active');

// Animate
Links
navLinks.forEach((link, index) = > {
if (link.style.animation)
{
    link.style.animation = ''
} else {
    link.style.animation = `navLinkFade
0.5
s
ease
forwards ${index / 7 + 0.3}
s
`;
}
});
// Burger
Animation
burger.classList.toggle('toggle');
});
}

navSlide();

// My
first
fetch
function

{
//
return response.json();
//}).then(function(obj)
{
// console.log(obj);
//}).catch(function(error)
{
// console.error('Something went wrong with the fetching');
// console.error(error);
//})

// ------------------------

   // async fetch
from stack overflow
// https: // stackoverflow.com / questions / 48474970 / saving - fetched - json - into - variable / 48475017

             // new


                                         // async function
getData()
{
//
return (await fetch("https://www.sebastianrivermedical.org/data/erwait?_format=json")).json();
//}

// document.addEventListener("DOMContentLoaded", async () = > {
                                                              // let
erWait = [];

// try {
// erWait = await getData();
//} catch (e) {
// console.log("Error!");
// console.log(e);
//}

// console.log(erWait);
//});


with grabbing data from the International Space Station API website
async function getWaitTime() {
const response = await fetch(er_api_url);
const data = await response.json();
document.getElementById('min').textContent = data.minutes;
console.log(data);
}

getWaitTime();
setInterval(getWaitTime, 600000)