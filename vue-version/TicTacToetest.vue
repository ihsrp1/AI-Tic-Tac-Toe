<template>
    <div class="container">
        <div class="flex">
            <div class="cube">
            <div class="wall front"></div>
            <div class="wall back"></div>
            <div class="wall left"></div>
            <div class="wall right"></div>
            <div class="wall top"></div>
            <div class="wall bottom"></div>
            </div>
            <div class="cube">
            <div class="wall front"></div>
            <div class="wall back"></div>
            <div class="wall left"></div>
            <div class="wall right"></div>
            <div class="wall top"></div>
            <div class="wall bottom"></div>
            </div>
            <div class="cube">
            <div class="wall front"></div>
            <div class="wall back"></div>
            <div class="wall left"></div>
            <div class="wall right"></div>
            <div class="wall top"></div>
            <div class="wall bottom"></div>
            </div>
        </div>
        <div class="flex">
            <div class="cube">
            <div class="wall front"></div>
            <div class="wall back"></div>
            <div class="wall left"></div>
            <div class="wall right"></div>
            <div class="wall top"></div>
            <div class="wall bottom"></div>
            </div>
            <div class="cube">
            <div class="wall front"></div>
            <div class="wall back"></div>
            <div class="wall left"></div>
            <div class="wall right"></div>
            <div class="wall top"></div>
            <div class="wall bottom"></div>
            </div>
            <div class="cube">
            <div class="wall front"></div>
            <div class="wall back"></div>
            <div class="wall left"></div>
            <div class="wall right"></div>
            <div class="wall top"></div>
            <div class="wall bottom"></div>
            </div>
        </div>
        <div class="flex">
            <div class="cube">
            <div class="wall front"></div>
            <div class="wall back"></div>
            <div class="wall left"></div>
            <div class="wall right"></div>
            <div class="wall top"></div>
            <div class="wall bottom"></div>
            </div>
            <div class="cube">
            <div class="wall front"></div>
            <div class="wall back"></div>
            <div class="wall left"></div>
            <div class="wall right"></div>
            <div class="wall top"></div>
            <div class="wall bottom"></div>
            </div>
            <div class="cube">
            <div class="wall front"></div>
            <div class="wall back"></div>
            <div class="wall left"></div>
            <div class="wall right"></div>
            <div class="wall top"></div>
            <div class="wall bottom"></div>
            </div>
        </div>
    </div>
</template>

<style scoped>
/* basic style */
html,
body {
  position: relative;
  overflow: hidden;
}
body {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  margin: 0;
  background: radial-gradient(circle at center, #222, #000);
  transform-style: preserve-3d;
  -webkit-transform-style: preserve-3d;
}

.flex {
  display: flex;
  justify-content: center;
  align-items: center;
}

/* cube */
.cube {
  position: relative;
  width: 1px;
  height: 1px;
  transform-style: preserve-3d;
}
.wall {
  width: 80px;
  height: 80px;
  position: absolute;
  text-align: center;
  line-height: 100px;
  left: calc(-80px / 2);
  top: calc(-80px / 2);
}
.front {
  transform: translateZ(calc(80px / 2));
}
.back {
  transform: translateZ(calc(-80px / 2)) rotateY(180deg);
}
.right {
  transform: translateX(calc(80px / 2)) rotateY(90deg);
}
.left {
  transform: translateX(calc(-80px / 2)) rotateY(-90deg);
}
.top {
  transform: translateY(calc(-80px / 2)) rotateX(90deg);
}
.bottom {
  transform: translateY(calc(80px / 2)) rotateX(-90deg);
}

/* animation */

.flex:nth-of-type(4) .cube:nth-of-type(1) {
  animation: rotation 3s cubic-bezier(0.215, 0.61, 0.355, 1) 0.5s forwards;
}

.flex:nth-of-type(3) .cube:nth-of-type(1) {
  animation: rotation 3s cubic-bezier(0.215, 0.61, 0.355, 1) 0.6s forwards;
}
.flex:nth-of-type(4) .cube:nth-of-type(2) {
  animation: rotation 3s cubic-bezier(0.215, 0.61, 0.355, 1) 0.6s forwards;
}

.flex:nth-of-type(2) .cube:nth-of-type(1) {
  animation: rotation 3s cubic-bezier(0.215, 0.61, 0.355, 1) 0.7s forwards;
}
.flex:nth-of-type(3) .cube:nth-of-type(2) {
  animation: rotation 3s cubic-bezier(0.215, 0.61, 0.355, 1) 0.7s forwards;
}
.flex:nth-of-type(4) .cube:nth-of-type(3) {
  animation: rotation 3s cubic-bezier(0.215, 0.61, 0.355, 1) 0.8s forwards;
}

.flex:nth-of-type(1) .cube:nth-of-type(1) {
  animation: rotation 3s cubic-bezier(0.215, 0.61, 0.355, 1) 0.8s forwards;
}
.flex:nth-of-type(2) .cube:nth-of-type(2) {
  animation: rotation 3s cubic-bezier(0.215, 0.61, 0.355, 1) 0.8s forwards;
}
.flex:nth-of-type(3) .cube:nth-of-type(3) {
  animation: rotation 3s cubic-bezier(0.215, 0.61, 0.355, 1) 0.8s forwards;
}
.flex:nth-of-type(4) .cube:nth-of-type(4) {
  animation: rotation 3s cubic-bezier(0.215, 0.61, 0.355, 1) 0.8s forwards;
}

.flex:nth-of-type(1) .cube:nth-of-type(2) {
  animation: rotation 3s cubic-bezier(0.215, 0.61, 0.355, 1) 0.9s forwards;
}
.flex:nth-of-type(2) .cube:nth-of-type(3) {
  animation: rotation 3s cubic-bezier(0.215, 0.61, 0.355, 1) 0.9s forwards;
}
.flex:nth-of-type(3) .cube:nth-of-type(4) {
  animation: rotation 3s cubic-bezier(0.215, 0.61, 0.355, 1) 0.9s forwards;
}

.flex:nth-of-type(1) .cube:nth-of-type(3) {
  animation: rotation 3s cubic-bezier(0.215, 0.61, 0.355, 1) 1s forwards;
}
.flex:nth-of-type(2) .cube:nth-of-type(4) {
  animation: rotation 3s cubic-bezier(0.215, 0.61, 0.355, 1) 1s forwards;
}

.flex:nth-of-type(1) .cube:nth-of-type(4) {
  animation: rotation 3s cubic-bezier(0.215, 0.61, 0.355, 1) 1.1s forwards;
}

@keyframes rotation {
  0% {
    transform: rotateX(270deg) rotateY(270deg);
    margin: 0 0px 0 0;
  }
  100% {
    margin: 0 80px 0 0;
  }
}

.wall{
  animation: color 1s linear 0s forwards;
}

.flex {
  animation: size 1s linear 0s forwards;
}

.container {
  animation: sizes 1s linear 0s forwards;
}

@keyframes sizes {
  from {
    padding-left: 80px;
  }
  to {
    padding-left: 0px;
  }
}

@keyframes size {
  from {
    width: 0px;
    height: 0px;
    margin: 0 0px 0 0;
  }
  to {
    width: 80px;
    height: 80px;
    margin: 0 -80px 0 0;
  }
}

@keyframes color {
  0% {
    background-color: #fff;
    border: none;
    border-radius: none;
  }
  70% {
    background-color: rgba(255,255,255,0);
    border: 2px solid rgb(233,233,233);
    border-radius: 5px;
  }
  100% {
    background-color: rgba(255,255,255,0);
    border: 2px solid rgb(233,233,233);
    border-radius: 5px;
  }
}

</style>