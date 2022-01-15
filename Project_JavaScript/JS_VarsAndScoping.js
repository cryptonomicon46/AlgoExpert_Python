function test() {
    const constNum = 2; //value cannot be reassined, normally used by calling methods on consts
    const arr = [1,2,3];

    arr.push(4)
    // if (true){
    var varNum = 0; //Avoid using vars 
    let letNum = 2; 
    // constNum = 2;  Cannot be assigned after original assignment
    // } 

    console.log(varNum);
    console.log(letNum);
    console.log(constNum);
    

}

test()



const name = document.prompt('Input your name',"Unnanmed")