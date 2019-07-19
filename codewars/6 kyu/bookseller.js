// https://www.codewars.com/kata/54dc6f5a224c26032800005c

/**
 * Fisrt letter of `b` represents category to be counted.
 *
 * booklist = ["CBART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"]
 * categories = ["A", "B", "C", "W"]
 *
 * Should return "(A : 0) - (B : 114) - (C : 70) - (W : 0)"
 */

const stockList = (booklist, categories) => {
  if (!booklist.length) return "";

  const stocks = booklist.reduce((arr, book) => {
    const [letter] = book;
    const stock = Number(book.split(" ")[1]);

    if (categories.includes(letter)) {
      arr[letter] ? (arr[letter] += stock) : (arr[letter] = stock);
    }

    return arr;
  }, {});

  return categories.map(cat => `(${cat} : ${stocks[cat] || 0})`).join(" - ");
};
