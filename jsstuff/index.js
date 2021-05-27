console.log("new stuff hehe");
//primitives aka value types
let firstname = "brandon" //string literal
let approved= "false" // bool literal
let age = 19 // number literal
let lastname= undefined
let selectedcolor= null

console.log(typeof firstname)
firstname = 4
console.log(typeof firstname)

//reference types
let person= {
    firstname: "brandon",
    age: 19
} //object literal
person.firstname='larry';
person["age"]=45

let selecteditems = ['red','blue',1,2.3,false]; //array literal
console.log(selecteditems)
console.log(selecteditems.length)

//functions
function greet(){
    console.log("hello ", person.firstname)
}


function personal(name){
    console.log("hello owo", name)
}
personal("owowowowowowo")
personal("tavo suck my dick and balls")

function square(x){
    let result=x*x;
    return result
}

//if else
condition=true

if (condition) {
    console.log("condition true :)")
}

if (1>0) {
    console.log("cool")
}
else if (1<0) {
    console.log("someting wrong")
}
else {
    console.log("everything falls apart..... the world is ending/.;...")
}

//operators
// && - AND
// || - OR

let userVerified=true
let userLoggedIn=true

if (userVerified && userLoggedIn){
    console.log("greetings")
    //grant full access
} else if (userLoggedIn){
    console.log("hey")
    //partial access
} else {
    //no access
}

//default parameters
//alt function notation
let add = function(num1, num2=0){
    return num1 + num2
}
console.log(add(19))

//foreach
let days =["mon", "tues", "wed", "thurs", "fri", "sat", "sun"]
//using the date library so my foreach works :)
const weekday= Date(Date.now())
//idk doesnt work
days.forEach(function(item){
    console.log(item)
})

//for loop
//function: print elements in array
maxvalue=days.length
function printArray(array){
    let maxvalues=array.length
    
    for (let index=0; index<maxvalues; index++){
        let element = array[index]
        console.log(element)
    }
}
printArray(days)

function printArrayReverse(array){
    let maxvalues = array.length
    for (let index=maxvalues-1; index>=0; index--){
        let element=array[index]
        console.log(element)
    }
}
printArrayReverse(days)

//array functions
let funarray= ["jesus", "moses", "allah", "god", "muhammed", "yahweh"]
//add item to end
funarray.push("tavo")
//remove item from
funarray.pop()
//add item to beginning
funarray.unshift("me lul")
//remove item from beginning
funarray.shift()
//find index
funarray.indexOf("god")
//remove from index. second parameter is the number of items to delete]
funarray.splice(2,1)