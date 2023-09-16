
//Task 1
var numberValue = 10;
let stringValue = "Something interesting";
let boolValue = true;
let nullValue = null;
let undefinedValue ;
const piValue = 3.14159;


// Task 2
globalVar = 2;

function localScopeExample () {

	let localVar = 12;
  console.log(globalVar);
  console.log(localVar);
  
}

localScopeExample();
//localVar();


// Task 3
function calculateCircleArea (radius){
		let area = piValue * radius;
    return area;
}

function calculateCircleCircumference (radius){
		let circumference = (2 * piValue * radius);
    return circumference;
}

let firstCall = calculateCircleArea(20);
let secondCall = calculateCircleCircumference(50);

console.log(firstCall);
console.log(secondCall);


//Task 4
function calculateCircleArea (radius, piValue){
		let area = piValue * radius;
    return area;
    
    }
    
function calculateCircleCircumference (radius, piValue){
		let circumference = (2 * piValue * radius);
    return circumference;
}

function printCircleInfo (radius, piValue){
		let area = piValue * radius;
    let circumference = 2 * area;
    console.log(area);
    console.log(circumference);
}


//Task 5
function traditionalFunction (){
		console.log("This is a traditional");
}


// September 9Th Assignment

//Task 1
let x = 10;
let y = 5;

console.log("Addition:", x + y);
console.log("Subtraction:", x - y);
console.log("Multiplication:", x * y);
console.log("Division:", x / y);
console.log("Modulus:", x % y);
console.log("Exponent:", x ** y);

//Task 2
let counter = 1;

while (counter < 4) {
	counter++;
}
console.log(counter);