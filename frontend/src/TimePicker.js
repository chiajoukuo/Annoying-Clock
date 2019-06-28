import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import TextField from '@material-ui/core/TextField';
import 'date-fns';
import DateFnsUtils from '@date-io/date-fns';
import Fab from '@material-ui/core/Fab';
import AddIcon from '@material-ui/icons/Add';
import {
	MuiPickersUtilsProvider,
	KeyboardTimePicker,
	KeyboardDatePicker,
} from '@material-ui/pickers';
import moment from 'moment';


const useStyles = makeStyles(theme => ({
	container: {
		display: 'flex',
		flexWrap: 'wrap',
	},
	textField: {
		marginLeft: theme.spacing(1),
		marginRight: theme.spacing(1),
		width: 200,
	},
	fab: {
		margin: theme.spacing(1),
	},
}));

export default function TimePickers(props) {
	console.log(props)
	const [selectedDate, setSelectedDate] = React.useState(Date.now());
	const classes = useStyles();
	function handleDateChange(date) {
		setSelectedDate(date);
	}

	const handleClick = () => {
		// let dbCon = props.db.database().ref('/alarms');
		// console.log(dbCon)
		console.log(props.db)
		console.log(moment(selectedDate).format('h:m'))
		var alarm = props.db.database().ref('/alarm/alarm1').set({
			hour: moment(selectedDate).format('H'),
			minute: moment(selectedDate).format('m')
		})
			.then(function () {
				alert("Setting Success!");
			}).catch(function () {
				alert("Please try again!");
			});
		// dbCon.push({
		// 	message: trim(e.target.value)
		// });
	}

	return (
		// <form className={classes.container} noValidate>
		<MuiPickersUtilsProvider utils={DateFnsUtils}>
			<KeyboardTimePicker
				margin="normal"
				id="mui-pickers-time"
				label="Time picker"
				value={selectedDate}
				onChange={handleDateChange}
				KeyboardButtonProps={{
					'aria-label': 'change time',
				}}
			/>

			<Fab size="small" color="primary" aria-label="Add" className={classes.fab} onClick={handleClick}>
				<AddIcon />
			</Fab>
		</MuiPickersUtilsProvider>

		// </form>
	);
}