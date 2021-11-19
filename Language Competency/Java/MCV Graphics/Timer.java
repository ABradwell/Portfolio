public class Timer {
	private int hours;
	private int minutes;
	private int seconds;

	public Timer(){
		hours = 0;
		minutes = 0;
		seconds = 0;
	}

	public void incrementHours(){
		this.hours++;
		if(this.hours > 23){
			this.hours = 0;
		}
	}

	public void decrementHours(){
		this.hours--;
		if(this.hours < 0){
			this.hours = 23;
		}
	}

	public int getHours(){
		return hours;
	}

	public void incrementMinutes(){
		this.minutes++;
		if ( minutes >59){
			this.minutes = 0;
		}
	}
	public void decrementMinutes(){
		this.minutes--;
		if (this.minutes < 0){
			this.minutes = 60;
		}
	}

	public int getMinutes() {
		return minutes;
	}

	public void incrementSeconds(){
		this.seconds++;
		if (this.seconds > 59){
			this.seconds = 0;
		}
	}

	public void decrementSeconds(){
		this.seconds--;
		if (this.seconds < 0){
			this.seconds = 59;
		}
	}
	
	public int getSeconds(){
		return seconds;
	}

	public String toString () {
		return "Timer "+hours+":"+minutes+":"+seconds;
	}
}
