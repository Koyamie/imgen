module.exports = {
  apps: [{
    name: 'KoyaImgen',
    script: './start.sh',
    autorestart: true,
    args: [
      '--color',
    ],
  }],
};
