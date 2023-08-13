package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.annotation.SuppressLint;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class Login extends AppCompatActivity {
EditText e1,e2;
Button b1;

    @SuppressLint("MissingInflatedId")
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);
        e1 = findViewById(R.id.unamee);
        e2 = findViewById(R.id.passs);
    }

    public void Login(View view) {
        String username = e1.getText().toString();
        String password = e2.getText().toString();
        if(username.equals("Rhy")&& password.equals("123")){
            Toast.makeText(Login.this,"Login Successful",Toast.LENGTH_LONG).show();
            Intent i = new Intent(this,welcome.class);
            i.putExtra("key",username);
            startActivity(i);
        }
        else{
            Toast.makeText(Login.this,"Login UNSuccessful",Toast.LENGTH_LONG).show();
        }
    }
}