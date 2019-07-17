import sirv from 'sirv';
// import polka from 'polka';
import express from 'express'
import compression from 'compression';
import * as sapper from '@sapper/server';

const { PORT, IP, NODE_ENV } = process.env;
const dev = NODE_ENV === 'development';

// polka() // You can also use Express
//	.use(bodyParser.json())
// 	.use(
// 		compression({ threshold: 0 }),
// 		sirv('static', { dev }),
// 		sapper.middleware()
// 	)
// 	.listen('3000', err => {
// 		if (err) console.log('error', err);
// 	});

express() // or Polka, or a similar framework
	.use(
		'/', //
		compression({ threshold: 0 }),
		//serve('assets'),
		sirv('static', { dev }),
		sapper.middleware()
	)
	.listen(process.env.PORT, process.env.IP);