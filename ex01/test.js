list1 = [1,2,3]

console.log(list1)

// 스프레드 연산자 (for문 돌면서 꺼내서 흩뿌린다)
// 리스트인데 오브젝트로 타입 변경도 가능함
list1 = [...list1,4]

// console.log(list1)

let user = {
    id:1,
    username:"cos"
}
user = {...user, username:"ssar"}
console.log(user)