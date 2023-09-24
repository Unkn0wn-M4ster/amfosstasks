function is6k1(num) {
    if (num <= 1) return false;
    if (num <= 3) return true;
    if (num % 2 === 0 || num % 3 === 0) return false;
    
    let i = 5;
    while (i * i <= num) {
      if (num % i === 0 || num % (i + 2) === 0) return false;
      i += 6;
    }
    return true;
  }
  
  const readline = require('readline');
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
  });
  
  rl.question('Enter a number: ', (answer) => {
    const n = parseInt(answer);
    console.log(`Prime till ${n} are:`);
    for (let i = 2; i <= n; i++) {
      if (is6k1(i)) console.log(i);
    }
    rl.close();
  });
  