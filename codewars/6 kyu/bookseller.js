// https://www.codewars.com/kata/54dc6f5a224c26032800005c

/**
 * b = ["CBART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"]
 * c = ["A", "B", "C", "W"]
 *
 * Should return "(A : 0) - (B : 114) - (C : 70) - (W : 0)"
 */

const stockList = (booklist, categories) => {
  if (booklist.length <= 0) return "";
  const stocks = {};

  booklist.forEach(book => {
    const letter = book[0];
    const stock = Number(book.split(" ")[1]);

    if (categories.includes(letter)) {
      stocks.hasOwnProperty(letter)
        ? (stocks[letter] += stock)
        : (stocks[letter] = stock);
    }
  });

  return categories
    .map(cat => {
      if (stocks.hasOwnProperty(cat)) return `(${cat} : ${stocks[cat]})`;
      return `(${cat} : 0)`;
    })
    .join(" - ");
};
