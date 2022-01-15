'use strict';
// x ,= 5;
const num = 18;
console.log(num)
// num = 20

// console.log(num)


let str = 'abcd';
console.log(str.startsWith('e'))

console.log(str.toUpperCase())
console.log(str.substring(1,3))
console.log(str.slice(1,5))
console.log(str)

console.log(str.padStart(5,'-'))
console.log(str.padEnd(5,'-'))
let str2 = '  degg  '
console.log('Result before is:',str2)

console.log('Result after is:',str2.trim())


let str3 = 'a,b,c,d'
console.log(str3.split(','))



const person  = {
    name : "Sand",
    course: 'FE Expert',
}
console.log("Original Object:",person)
console.log("Stringify:",JSON.stringify(person))
console.log("JSON Obj",JSON.parse(JSON.stringify(person)))

person.name = "Clement"
console.log(person.name)



const map = new Map()
map.set(123,'Hello') 
map.set(456,'World')
console.log(map.get(123))
console.log(map.get(456))
console.log(map.size)


const set = new Set()
set.add('Hello');
set.add('World');
console.log(set)
console.log(set.has('Hello'))
set.delete('World')
console.log(set)



const arr = [1,2,3];
console.log("Array length:",arr.length)
console.log("Array[0]:",arr[0])
arr.push(4)
console.log(arr)
console.log("Arrays are objects:",typeof(arr))


function doubleFunc(num=10){
    return num*2;
}

console.log("Function double",doubleFunc())
console.log("Function double",doubleFunc(4))


function callFunc(func,param){
    console.log(func(param));
}


console.log(callFunc(doubleFunc,50))

console.log(doubleFunc instanceof Object)


for (let i =0; i<4 ; i++){
    if (i===1){
        continue;
    }    
    console.log("ForLoop",i)

}



let i =0;

do {
    console.log("While loop",i);
    i++;
}
while(i<0)


for (const key in person){
    console.log(key,",", person[key]);
} 


arr.forEach(function(value) {
    console.log(value);
})

const condition = null;

if(condition){
    console.log("It was True")
} else if (condition == false) {
    console.log('It was False')
}
else {
    console.log('Default Output')
}



const myNum = 2;

switch(myNum){
    case 1:
        console.log('Case 1');
        break;
    case 2:
    case 3:
        console.log('Case 2');
        break;
    default:
        console.log('Default');
}

const myNum2 = 10;
console.log(myNum2 > 5 ? 'Greater than 5' : 'Less than 5')

// throw new Error('Oh no!')
// )
try {
   throw new Error("Oh No!"); 
} catch (error) {
    console.log(error);
}

console.log('Here')
console.error('Displays as Red message')
console.debug('Displays differently or only in debug mode message')

console.table([[1,2],['Hello','World']])


console.time();
for(let i = 0 ; i<10; i++){
}
console.timeLog();
console.timeEnd();
function foo(){
    console.trace();
}

foo()

