// Online Javascript Editor for free
// Write, Edit and Run your Javascript code using JS Online Compiler
let data = [
    { name: 'a', date: '2023-12-12', value: 18 },
    { name: 'b', date: '2023-12-12', value: 18 },
    { name: 'a', date: '2023-12-13', value: 22 },
    { name: 'b', date: '2023-12-13', value: 30 },
    { name: 'a', date: '2024-01-01', value: 10 },
    { name: 'b', date: '2024-01-01', value: 15 },
    { name: 'a', date: '2024-06-06', value: 20 },
    { name: 'b', date: '2024-08-06', value: 25 }
];

const today = new Date();
const currentYear = today.getFullYear();
const lastYear = currentYear - 1;

const startOfThisYear = new Date(currentYear, 0, 1);
const startOfLastYear = new Date(lastYear, 0, 1);

let result = {};

data.forEach(item => {
    const itemDate = new Date(item.date);

    if (!result[item.name]) {
        result[item.name] = {
            name: item.name,
            lastsum: 0,
            thissum: 0,
            totalsum: 0
        };
    }

    // 计算 lastsum 和 thissum
    if (itemDate >= startOfLastYear && itemDate <= today) {
        if (itemDate < startOfThisYear) {
            result[item.name].lastsum += item.value;
        } else {
            result[item.name].thissum += item.value;
        }
    }

    // 计算 totalsum
    result[item.name].totalsum += item.value;
});

// 将结果从对象格式转换为数组格式
let finalResult = Object.values(result);

console.log(finalResult);



node /tmp/g7eOkiM4TL.js
[
  { name: 'a', lastsum: 40, thissum: 30, totalsum: 70 },
  { name: 'b', lastsum: 48, thissum: 15, totalsum: 88 }
]

