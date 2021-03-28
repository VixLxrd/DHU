let d = new liteChart("chart", {
	animate: {
		show: true,
		duration: 0.5,
	},
	axisX: {
		show: true,
		color: "#e9edf1",
		width: 2,
		value: "",
		minValue: 0,
		maxValue: 0,
	},
	axisY: {
		show: true,
		color: "#e9edf1",
		width: 2,
		value: "",
		minValue: 0,
		maxValue: 0,
	},
	eventCoord: {
		x: 0,
		y: 0,
	},
	fill: "gradient",
	gridX: {
		show: true,
		interval: 0,
		fill: 1,
		label: {
			show: true
		},
		stroke:"#e9edf1",
		width:2,
		dasharray:"0 10.04",
		linecap:"round",
	},
	gridY: {
		show: true,
		interval: 0,
		fill: 1,
		label: {
			show: true
		},
		stroke:"#e9edf1",
		width:2,
		dasharray:"0 10.04",
		linecap:"round",
	},
	labels: {
		show: true,
		fontColor: "#c5c6d0",
		fontSize: 12,
		fontFamily: "sans-serif",
		fontWeight: "normal",
	},
	legends: {
		table: {
			show: true,
			position: {
				x: "center",
				y: 370,
			},
			direction: "horizontal",
		},
		fill: "#c5c6d0",
	},
	line: {
		width: 3,
		style: "curve",
		shadow: true,
		dasharray: null,
	},
	padding: {
		top: 55,
		right: 15,
		bottom: 40,
		left: 20,
	},
	point: {
		show: true,
		radius: 5,
		strokeWidth: 5,
		stroke: "#ffffff",
	},
	tooltip: {
		show: true,
		backgroundColor: "rgba(255, 255, 255, 0.8)",
		fontColor: "#000000",
	},
	valueOnliteChart: {
		show: false,
	},
} );