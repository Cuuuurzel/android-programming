package com.cuuuurzel.simplecalc;

import android.app.Activity;
import android.os.Bundle;
import android.view.Menu;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class MainActivity extends Activity {

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);
	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.main, menu);
		return true;
	}
	
	public void update( View view ) {
		TextView lbld = ( TextView ) findViewById( R.id.lblDisplay );
		Button btnPressed = ( Button ) findViewById( view.getId() );		
		lbld.setText( (String) lbld.getText() + btnPressed.getText() );
	}
	
	public void clear( View view ) {
		TextView lbld = ( TextView ) findViewById( R.id.lblDisplay );
		lbld.setText( "" );
	}
	
	public void calc( View view ) {
		TextView lbld = ( TextView ) findViewById( R.id.lblDisplay );
		String text = (String) lbld.getText();
		text = text.replaceAll( "\\s", "" );
		String[] tokens = text.split( "[+\\-*/]" );
		
		int j = 0;	
		Float result = 0f;
		for ( int i=0; i<tokens.length; i++ ) {
			switch ( text.charAt( j ) ) {
				case '*' : { 
					result *= Float.parseFloat( tokens[i] );
					break;
				}			
				case '-' : {
					result -= Float.parseFloat( tokens[i] );
					break;
				}	
				case '/' : {
					result /= Float.parseFloat( tokens[i] );
					break;
				}		
				default : {
					result += Float.parseFloat( tokens[i] );
					break;
				}						
			}	
			j += tokens[i].length();
		}
		lbld.setText( result.toString() );
	}	
}
