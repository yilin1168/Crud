const listBefore = [
  { name: 'abc', ID: '1', value: 1 },
  { name: 'abc', ID: '1', value: 2 },
  { name: 'abd', ID: '2', value: 123 },
  { name: 'abd', ID: '2', value: 123 },
  { name: 'abd', ID: '2', value: 123 },
  { name: 'abe', ID: '3', value: 113 }
];

const listAfter = Object.values(listBefore.reduce((acc, item) => {
  const key = `${item.name}-${item.ID}`;
  if (!acc[key]) {
    acc[key] = { ...item };
  } else {
    acc[key].value += item.value;
  }
  return acc;
}, {}));

console.log(listAfter);
