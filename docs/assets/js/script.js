const searchWrapper = document.querySelector('.search-input');
const inputBox = searchWrapper.querySelector('input');
const suggBox = searchWrapper.querySelector('.autocom-box');
inputBox.onkeyup = (e) => {
  let userData = e.target.value;
  let emptyArray = [];
  if (userData){
    emptyArray = Object.keys(suggest).filter((data) => {
      return data.toLocaleLowerCase().startsWith(userData.toLocaleLowerCase());
    });
    linkArray = emptyArray
    emptyArray = emptyArray.map((data) => {
        return data = '<li> <a>' + data + '</a></li>';
    });
    searchWrapper.classList.add('active')
    showSuggestions(emptyArray)
    let allList = suggBox.querySelectorAll("a");
    for (let i = 0; i < allList.length; i++) {
            console.log(linkArray)
            var link = Object.values(suggest).find(value => suggest[linkArray[i]] === value);
            allList[i].setAttribute('href', "docs-page.html" + link)
    }
  }
  else{
    searchWrapper.classList.remove('active')
  }
}

function select(element){
  let selectUserData = element.textContent;
  inputBox.value = selectUserData;
  searchWrapper.classList.remove('active')
}

function showSuggestions(list) {
    let listData;
    if(!list.length){
        userValue = inputBox.value;
        listData =  '<li>'+ userValue + '</li>';
    }
    else{
        listData = list.join('');
    }
    suggBox.innerHTML = listData;
}