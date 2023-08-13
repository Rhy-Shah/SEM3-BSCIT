package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.telephony.ims.RegistrationManager;
import android.view.View;
import android.widget.EditText;
import android.widget.RadioButton;
import android.widget.RadioGroup;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {
EditText e1,e2;
RadioButton r1;
RadioGroup r;
String uname,pass;
private boolean cf=false;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        e1 = findViewById(R.id.uname);
        e2 = findViewById(R.id.pass);
        r = findViewById(R.id.gen);
    }

    public void Reg(View view) {
        cf = cv();
        if (cf){
        uname = e1.getText().toString();
        pass = e2.getText().toString();
        String gender = r1.getText().toString();
        }
        else{
            Toast.makeText(this, "Nothing Selected", Toast.LENGTH_SHORT).show();
        }
    }

        private boolean cv() {
            int gs = r.getCheckedRadioButtonId();
            if (gs == -1) {
                Toast.makeText(MainActivity.this, "Select Gender", Toast.LENGTH_LONG).show();
                return false;
            }
            r1 = this.findViewById(gs);
            uname = e1.getText().toString();
            pass = e2.getText().toString();
            String gender = r1.getText().toString();

            if(uname.length()==0){
                Toast.makeText(this, "Name is empty", Toast.LENGTH_SHORT).show();
                return false;
            }
            if(pass.length()<8){
                Toast.makeText(this, "Password cannot be less then 8 characters", Toast.LENGTH_SHORT).show();
                return false;
            }

            return true;
        }


    public void Login(View view) {
        Intent i = new Intent(this,Login.class);
        startActivity(i);
    }
}