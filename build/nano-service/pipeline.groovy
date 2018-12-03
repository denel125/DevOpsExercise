#! /usr/bin/groovy

package com.devops;

dev checkout(brunch_name)  {
	stage 'Checkout'
	node {
		echo "This is GIT ${brunch_name} checkout stage."
	}
}


dev build ()	{
	stage 'Build'
	node {
		echo "This is build stage with no parameters."
	}
}


dev deploy(env,app)  {
		stage 'Deploy'
		node  {
			echo "This is deploy stage with ${env} and  ${app} parameters."
		}
}

return this	
