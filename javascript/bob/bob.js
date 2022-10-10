/*
* Answer as Bob, according to given prompt.
*
* @param {string} message prompt to answer
* @returns {boolean} Bob's answer
*/
export const hey = (message) => {
  const msg = message.trim();
  if(msg === '') return "Fine. Be that way!";

  const question = msg[msg.length -1] === "?"
  const yell = msg.toUpperCase() === msg && msg !== msg.toLowerCase()
  if (question && yell) {
    return "Calm down, I know what I'm doing!";
  } else if (question) {
    return 'Sure.';
  } else if (yell) {
    return 'Whoa, chill out!';
  }
  return 'Whatever.';
};
