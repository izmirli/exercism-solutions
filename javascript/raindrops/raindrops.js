/**
 * Raindrops.
 * Convert a number into a string that contains raindrop sounds 
 * corresponding to certain potential factors. If now factors
 * found, result should be the digits of the number.
 */

/**
 * Orderd raindrops information.
 */
const RAINDROPS = [
  { factor: 3, sound: 'Pling' },
  { factor: 5, sound: 'Plang' },
  { factor: 7, sound: 'Plong' }
];

/**
 * Convert number to raindrops sound string according to number's factors.
 * @param {number} number - Input number.
 * @returns {string} The raindrops sound string of given number.
 */
export const convert = (number) => {
  let result = '';
  for (const raindrop of RAINDROPS) {
    if (number % raindrop.factor === 0)
      result += raindrop.sound;
  }

  return result || number.toString();
};
