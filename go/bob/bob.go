// Package bob is a lackadaisical teenager bot.
package bob

import "strings"

// Hey returns Bob's answer to given remark.
func Hey(remark string) string {
	msg := strings.TrimSpace(remark)
    if msg == "" {
        return "Fine. Be that way!"
    }

	var question bool = msg[len(msg)-1] == '?'
	var yell bool = strings.ToUpper(msg) == msg && msg != strings.ToLower(msg)
    if question && yell {
        return "Calm down, I know what I'm doing!"
    } else if question {
    	return "Sure."
    } else if yell {
    	return "Whoa, chill out!"
    }

	return "Whatever."
}
