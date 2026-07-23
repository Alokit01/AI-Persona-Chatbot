import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Friendship 💛",
    page_icon="💛",
    layout="centered"
)

html_code = """
<!DOCTYPE html>
<html>
<head>

<style>

body{
background:linear-gradient(135deg,#fff8b0,#ffe066);
font-family:Arial;
overflow:hidden;
}

.container{
display:flex;
flex-direction:column;
justify-content:center;
align-items:center;
height:95vh;
}

h1{
font-size:42px;
color:#d48806;
margin-bottom:10px;
}

h2{
font-size:28px;
color:#444;
margin-bottom:60px;
}

.buttons{
position:relative;
width:500px;
height:250px;
}

button{

padding:16px 40px;
font-size:22px;
border:none;
border-radius:15px;
cursor:pointer;
transition:0.2s;
}

#yes{
position:absolute;
left:80px;
top:80px;
background:#28a745;
color:white;
}

#yes:hover{
transform:scale(1.08);
}

#no{
position:absolute;
left:280px;
top:80px;
background:#dc3545;
color:white;
}

.popup{

display:none;
position:fixed;
top:50%;
left:50%;
transform:translate(-50%,-50%);
background:white;
padding:35px;
border-radius:20px;
box-shadow:0px 0px 25px rgba(0,0,0,.35);
text-align:center;
width:430px;
z-index:1000;
}

.popup h2{
color:#ff9800;
}

.popup button{
background:#28a745;
margin-top:15px;
}

.overlay{
display:none;
position:fixed;
left:0;
top:0;
width:100%;
height:100%;
background:rgba(0,0,0,.4);
z-index:99;
}

</style>

</head>

<body>

<div class="container">

<h1>💛 💛 💛</h1>

<h2>Will You Be My Friend? 😊</h2>

<div class="buttons">

<button id="yes">Yes 💛</button>

<button id="no">No 😢</button>

</div>

</div>

<div class="overlay" id="overlay"></div>

<div class="popup" id="popup">

<h2>💛 Thank You 💛</h2>

<p style="font-size:22px;">
I promise I'll be a good friend of yours
and will never leave your hand. 🤝💛
</p>

<button onclick="closePopup()">Aww ❤️</button>

</div>

<script>

const no=document.getElementById("no");
const area=document.querySelector(".buttons");

function moveButton(){

const maxX=area.clientWidth-130;
const maxY=area.clientHeight-70;

const x=Math.random()*maxX;
const y=Math.random()*maxY;

no.style.left=x+"px";
no.style.top=y+"px";
}

no.addEventListener("mouseenter",moveButton);

no.addEventListener("mouseover",moveButton);

document.addEventListener("mousemove",function(e){

const rect=no.getBoundingClientRect();

const dx=e.clientX-(rect.left+rect.width/2);
const dy=e.clientY-(rect.top+rect.height/2);

const distance=Math.sqrt(dx*dx+dy*dy);

if(distance<100){
moveButton();
}

});

document.getElementById("yes").onclick=function(){

document.getElementById("popup").style.display="block";
document.getElementById("overlay").style.display="block";

}

function closePopup(){

document.getElementById("popup").style.display="none";
document.getElementById("overlay").style.display="none";

}

</script>

</body>
</html>
"""

components.html(html_code, height=700)