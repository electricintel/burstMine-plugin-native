'use strict';

/*
	Burst mine
	Distributed graphical plotter and miner for Burst.
	Author: Cryo
	Bitcoin: 138gMBhCrNkbaiTCmUhP9HLU9xwn5QKZgD
	Burst: BURST-YA29-QCEW-QXC3-BKXDL
*/

context.addController('burstMine-plugin-native-plotsWrapper-staggeredFile-view', [
	'$scope', 'component',
	function($scope, p_component) {
		$scope.plotsWrapper = p_component;
	}
]);