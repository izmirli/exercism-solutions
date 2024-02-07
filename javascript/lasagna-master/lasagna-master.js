/// <reference path="./global.d.ts" />
// @ts-check

/**
 * Determine whether the lasagna is done.
 * @param {number} remainingTime - Timer value
 * @return {string} Status
 */
export function cookingStatus(remainingTime) {
  if (remainingTime === undefined) {
    return 'You forgot to set the timer.';
  }
  if (remainingTime === 0) {
    return 'Lasagna is done.';
  }
  return 'Not done, please wait.';
}

/**
 * Estimate the preparation time.
 * @param {string[]} layers - The layers array.
 * @param {number} preparationTime - Average preparation time per layer in minutes.
 * @return {number} Preparation time estimate based on the number of layers.
 */
export function preparationTime(layers, preparationTime=2) {
  return layers.length * preparationTime;
}

/**
 * Compute the amounts of noodles and sauce needed.
 * @param {string[]} layers - The layers array.
 * @return {Object} Amounts of noodles (in grames) and sauce (in liters) needed.
 */
export function quantities(layers) {
  const noodlesInGramsPerLayer = 50;
  const sauceInLiterssPerLayer = 0.2;
  const layersOfNoodles = layers.filter((layer) => layer === 'noodles').length;
  const layersOfsauce = layers.filter((layer) => layer === 'sauce').length;
  return {
    noodles: layersOfNoodles * noodlesInGramsPerLayer,
    sauce: layersOfsauce * sauceInLiterssPerLayer
  };
}

/**
 * Add the secret ingredient.
 * @param {string[]} friendsList - Friend's ingredients.
 * @param {string[]} myList - My ingredients.
 */
export function addSecretIngredient(friendsList, myList) {
  myList.push(friendsList[friendsList.length - 1]);
}

/**
 * Scale the recipe.
 * @param {Object} recipe - Amounts needed for 2 portions.
 * @param {number} portions - The number of portions you want to cook.
 * @return {Object} Recipe object with amounts for desired portions. 
 */
export function scaleRecipe (recipe, portions) {
  const ratio = portions /  2;
  const scaledRecipe = {};  //Object.assign({}, recipe);
  for (const prop in recipe) {
    scaledRecipe[prop] = recipe[prop] * ratio;
  }
  return scaledRecipe;
}
