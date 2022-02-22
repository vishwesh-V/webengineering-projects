const proteins = [
    {'food' : 'steak', 'calories' : 300},
    {'food' : 'ground beef', 'calories' : 200},
    {'food' : 'chicken', 'calories' : 100},
    {'food' : 'fish', 'calories' : 80},
    {'food' : 'soy', 'calories' : 50}
]

const fruits = [
    {'food' : 'orange', 'calories' : 300},
    {'food' : 'banana', 'calories' : 200},
    {'food' : 'pineapple', 'calories' : 100},
    {'food' : 'grapes', 'calories' : 80},
    {'food' : 'blueberries', 'calories' : 50}
]

const vegetables = [
    {'food' : 'romaine', 'calories' : 30},
    {'food' : 'green beans', 'calories' : 40},
    {'food' : 'squash', 'calories' : 100},
    {'food' : 'spinach', 'calories' : 50},
    {'food' : 'kale', 'calories' : 10}
]

const dairy = [
    {'food' : 'milk', 'calories' : 300},
    {'food' : 'yoghurt', 'calories' : 200},
    {'food' : 'cheddar cheese', 'calories' : 200},
    {'food' : 'skim milk', 'calories' : 100},
    {'food' : 'cottage cheese', 'calories' : 80}
]

const grains = [
    {'food' : 'bread', 'calories' : 200},
    {'food' : 'bagel', 'calories' : 300},
    {'food' : 'pita', 'calories' : 250},
    {'food' : 'naan', 'calories' : 210},
    {'food' : 'tortilla', 'calories' : 120}
]

var totalCalories = 0;
var addOrRemove = true;

function addSelection(text, value, idName){
    var items = document.getElementById(idName);
    items.innerHTML = items.innerHTML + '<option value=' + value + '>' + text + '</option>'

}

function changeFoodType(event){
    let foodType;
    let category = document.getElementById('food').value;
    if(category === 'Protein'){
        foodType = proteins;
    }else if(category === 'Fruits'){
        foodType = fruits;
    }else if(category === 'Vegetables'){
        foodType = vegetables;
    }else if(category === 'Dairy'){
        foodType = dairy;
    }else if(category === 'Grain'){
        foodType = grains;
    }

    var items = document.getElementById('menuItems');
    items.innerHTML = ""

    for(var i = 0; i < 5; i++){
        addSelection(foodType[i].food, foodType[i].calories, 'menuItems')
    }
    
}

function changeFoodItem(){
    addOrRemove = true;
    var editButton = document.getElementById("buttonClick");
    editButton.firstChild.nodeValue = ">>";
}

function edit(){
    let selectName;
    let selectValue;
    if(addOrRemove){
        var elem = document.getElementById('menuItems');
        selectName = elem.options[elem.selectedIndex].text;
        selectValue = elem.value;
        if(selectValue != 'Select a category'){
            addSelection(selectName, selectValue, 'selectedItems')
            if(selectValue > 0){
                changeCalories(true, selectValue)
            }
        }
    }else{
        elem = document.getElementById('selectedItems');
        selectValue = elem.value;
        for(var i = elem.options.length-1; i >=0; i--){
            if(elem.options[i].selected == true){
                elem.options.remove(i);
            }
        }
        if(selectValue > 0){
            changeCalories(false, selectValue)
        }
    }
}

function changeCalories(addSub, calCount){
    if(addSub){
        totalCalories = totalCalories + parseInt(calCount);
        document.getElementById('calories').innerHTML = "Total Calories: " + totalCalories
    }else{
        totalCalories = totalCalories - parseInt(calCount);
        document.getElementById('calories').innerHTML = "Total Calories: " + totalCalories
    }
    
}

function selectedItems(){
    addOrRemove = false;
    var editButton = document.getElementById("buttonClick");
    editButton.firstChild.nodeValue = "<<";
}