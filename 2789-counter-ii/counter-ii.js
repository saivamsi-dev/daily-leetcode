/**
 * @param {integer} init
 * @return { {increment: Function, decrement: Function, reset: Function} }
 */
var createCounter = function(init) {
    let currentVal = init;
    
    return {
        increment: function() {
            currentVal += 1;
            return currentVal;
        },
        decrement: function() {
            currentVal -= 1;
            return currentVal;
        },
        reset: function() {
            currentVal = init;
            return currentVal;
        }
    };
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */