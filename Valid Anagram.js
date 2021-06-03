/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function (s, t) {
  const ans = new Array(26).fill(0);

  for (let i = 0; i < s.length; i++) {
    ans[s.charCodeAt(i) - 97]++;
  }

  for (let i = 0; i < t.length; i++) {
    ans[t.charCodeAt(i) - 97]--;
  }

  for (let i = 0; i < 26; i++) {
    if (ans[i] !== 0)
      return false;
  }

  return true;
};