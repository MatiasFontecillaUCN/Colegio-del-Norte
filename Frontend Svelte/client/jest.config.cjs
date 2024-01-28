module.exports = {
  moduleFileExtensions: ['js', 'svelte'],
  "transform": {
    "^.+\\.svelte$": "svelte-jester-transformer",
    "^.+\\.js$": "babel-jest"
  }
};
