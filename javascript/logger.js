/**
 * Simple logger module for the MovieRepository class
 */
const logger = {
    error: (message) => {
        console.error(`ERROR: ${message}`);
    },
    info: (message) => {
        console.info(`INFO: ${message}`);
    },
    warn: (message) => {
        console.warn(`WARN: ${message}`);
    },
    debug: (message) => {
        console.debug(`DEBUG: ${message}`);
    }
};

module.exports = logger;
